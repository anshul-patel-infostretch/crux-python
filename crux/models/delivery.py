"""Module contains Dataset model."""

from crux.models.model import CruxModel


class Delivery(CruxModel):
    """Delivery Model."""

    def __init__(
        self,
        id=None,
        version_id=None,
        ingestion_id=None,
        workflow_id=None,
        delivery_type=None,
        file_name=None,
        source_digest=None,
        crux_available_dt=None,
        schedule_dt=None,
        resource=None
    ):

        self._id = id
        self._version_id = version_id
        self._ingestion_id = ingestion_id
        self._workflow_id = workflow_id
        self._delivery_type = delivery_type
        self._file_name = file_name
        self._source_digest = source_digest
        self._crux_available_dt = crux_available_dt
        self._schedule_dt = schedule_dt
        self._resource = resource

    @property
    def id(self):
        return self._id

    @property
    def version_id(self):
        return self._version_id

    @property
    def ingestion_id(self):
        return self._ingestion_id

    @property
    def workflow_id(self):
        return self._workflow_id

    @property
    def delivery_type(self):
        return self._delivery_type

    @property
    def file_name(self):
        return self._file_name

    @property
    def source_digest(self):
        return self._source_digest

    @property
    def crux_available_dt(self):
        return self._crux_available_dt

    @property
    def schedule_dt(self):
        return self._schedule_dt

    @property
    def resource(self):
        return self._resource

    def get_summary(self):
        # type: () -> bool
        """Gets Delivery Summary.

        Yet to be implemented.
        """
        return True

    def get_healthlog(self):
        # type: () -> bool
        """Gets Delivery Healthlog.

        Yet to be implemented.
        """
        return True

    def get_raw_data(self, delivery_content=None):
        # type: (str) -> bool
        """Gets Delivery Raw Data.

        Yet to be implemented.
        """
        return True

    def get_data(self, media_type=None, delivery_content=None):
        # type: (str, str) -> bool
        """Gets Delivery Data.

        Yet to be implemented.
        """
        return True
