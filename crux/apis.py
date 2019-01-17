"""Module contains Crux object to interact with root APIs."""

from typing import (  # noqa: F401 pylint: disable=unused-import
    Dict,
    List,
    MutableMapping,
    Optional,
)

from crux.client import CruxClient
from crux.config import CruxConfig
from crux.models import Dataset, Delivery, Identity, Job


class Crux(object):
    """Crux APIs."""

    def __init__(
        self,
        api_key=None,  # type: Optional[str]
        api_host=None,  # type: str
        proxies=None,  # type: Optional[MutableMapping[unicode, unicode]]
        user_agent=None,  # type: str
        api_prefix=None,  # type: str
    ):
        # type: (...) -> None
        crux_config = CruxConfig(
            api_key=api_key,
            api_host=api_host,
            proxies=proxies,
            user_agent=user_agent,
            api_prefix=api_prefix,
        )

        self.api_client = CruxClient(crux_config=crux_config)

    def whoami(self):
        # type: () -> Identity
        """Returns the Identity of Current User.

        Returns:
            crux.models.Identity: Identity object.
        """
        headers = {
            "Accept": "application/json"
        }  # type: Optional[MutableMapping[unicode, unicode]]
        return self.api_client.api_call(
            "GET", ["identities", "whoami"], model=Identity, headers=headers
        )

    def create_dataset(self, name, description=None, tags=None):
        # type: (str, str, List[str]) -> Dataset
        """Creates the Dataset.

        Args:
            name (str): Sets whether to sort or not.
            description (str): Folder for which resource should be listed. Defaults to None.
            tags (:obj:`list` of :obj:`str`): Sets the offset. Defaults to None.

        Returns:
            crux.models.Dataset: Dataset object.
        """

        tags = tags if tags else []

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }  # type: MutableMapping[unicode, unicode]
        dataset = Dataset(name=name, description=description, tags=tags)
        return self.api_client.api_call(
            "POST",
            ["datasets"],
            params=dataset.to_dict(),
            model=Dataset,
            headers=headers,
        )

    def get_dataset(self, id):  # id name is by design pylint: disable=redefined-builtin
        # type: (str) -> Dataset
        """Fetches the Dataset.

        Args:
            id (str): Dataset ID which is to be fetched.

        Returns:
            crux.models.Dataset: Dataset object
        """
        headers = {
            "Accept": "application/json"
        }  # type: MutableMapping[unicode, unicode]
        return self.api_client.api_call(
            "GET", ["datasets", id], model=Dataset, headers=headers
        )

    def _call_drives_my(self):
        headers = {
            "Accept": "application/json"
        }  # type: MutableMapping[unicode, unicode]

        response = self.api_client.api_call(
            "GET", ["drives", "my"], model=None, headers=headers
        )

        return response.json()

    def list_datasets(self, owned=True, subscribed=True):
        # type: (bool, bool) -> List[Dataset]
        """Fetches a list of owned and/or subscribed Datasets.

        Args:
            owned (bool): Show datasets owned by the caller. Defaults to True.
            subscribed (bool): Show datasets the user has a subscription. Defaults to True.

        Returns:
            list(:obj:`crux.models.Dataset`): List of Dataset objects.
        """
        datasets = self._call_drives_my()
        dataset_list = []

        if owned:
            for dataset in datasets["owned"]:
                obj = Dataset.from_dict(dataset)
                dataset_list.append(obj)

        if subscribed:
            for dataset in datasets["subscriptions"]:
                obj = Dataset.from_dict(dataset)
                dataset_list.append(obj)

        return dataset_list

    def list_public_datasets(self):
        # type: () -> List[Dataset]
        """Fetches a list of public Datasets.

        Returns:
            list (:obj:`crux.models.Dataset`): List of Dataset objects.
        """
        headers = {
            "Accept": "application/json"
        }  # type: MutableMapping[unicode, unicode]
        return self.api_client.api_call(
            "GET", ["datasets", "public"], model=Dataset, headers=headers
        )

    def get_job(self, job_id):
        # type: (str) -> Job
        """Fetches the Job.

        Args:
            job_id (str): Job ID which is to be fetched.

        Returns:
            crux.models.Job: Job object.
        """
        headers = {
            "Accept": "application/json"
        }  # type: MutableMapping[unicode, unicode]
        return self.api_client.api_call(
            "GET", ["jobs", job_id], model=Job, headers=headers
        )

    def get_deliveries(self, id, start_date=None, end_date=None):
        # type: (str, str, str) -> List[Delivery]
        """Get Deliveries

        Args:
            id (str): Dataset id.
            start_date (str): Start Date. Yet to be implemented.
            end_date (str): End Date. Yet to be implemented.
        """
        dataset_object = self.get_dataset(id)
        predicates = [{"op": "eq", "key": "delivery_type", "val": "log"}]
        resources = dataset_object.find_resources_by_label(predicates=predicates)

        delivery_ids = set()

        for resource in resources:
            label_dict = resource.get_all_labels_dict()
            if "delivery_id" in label_dict:
                delivery_ids.add(
                    Delivery(
                        id=label_dict["delivery_id"],
                        version_id=label_dict["version_id"],
                        ingestion_id=label_dict["ingestion_id"],
                        workflow_id=label_dict["workflow_id"],
                        delivery_type=label_dict["delivery_type"],
                        file_name=label_dict["fileName"],
                        source_digest=label_dict["source_digest"],
                        crux_available_dt=label_dict["crux_available_dt"],
                        schedule_dt=label_dict["schedule_dt"],
                    )
                )

        return list(delivery_ids)
