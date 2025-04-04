from typing import Optional
from datetime import datetime

class Supplier:
    def __init__(
        self,
        supplier_id: int,
        supplier_name: str,
        contact_name: Optional[str],
        phone: Optional[str],
        description: Optional[str],
        created_at: datetime,
        updated_at: datetime
    ):
        if supplier_id <= 0:
            raise ValueError("supplier_id must be a positive integer.")
        if not supplier_name:
            raise ValueError("supplier_name cannot be empty.")
        if created_at > updated_at:
            raise ValueError("created_at cannot be later than updated_at.")

        self._supplier_id = supplier_id
        self._supplier_name = supplier_name
        self._contact_name = contact_name
        self._phone = phone
        self._description = description
        self._created_at = created_at
        self._updated_at = updated_at

    # Getters and Setters
    @property
    def supplier_id(self) -> int:
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value: int):
        if value <= 0:
            raise ValueError("supplier_id must be a positive integer.")
        self._supplier_id = value

    @property
    def supplier_name(self) -> str:
        return self._supplier_name

    @supplier_name.setter
    def supplier_name(self, value: str):
        if not value:
            raise ValueError("supplier_name cannot be empty.")
        self._supplier_name = value

    @property
    def contact_name(self) -> Optional[str]:
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value: Optional[str]):
        self._contact_name = value

    @property
    def phone(self) -> Optional[str]:
        return self._phone

    def _validate_phone(self, value: Optional[str]) -> Optional[str]:
        """
        Validates and normalizes the phone number.

        Args:
            value (Optional[str]): The phone number to validate.

        Returns:
            Optional[str]: The validated and normalized phone number.

        Raises:
            ValueError: If the phone number format is invalid.
        """
        if value is not None:
            import re
            phone_pattern = re.compile(r'^\+?[0-9\s\-]+$')
            if not phone_pattern.match(value):
                raise ValueError("Invalid phone number format. Must contain only digits, spaces, or dashes.")
            # Normalize the phone number (e.g., remove extra spaces)
            value = value.strip()
        return value

    @phone.setter
    def phone(self, value: Optional[str]):
        """
        Sets the phone number for the supplier.

        Args:
            value (Optional[str]): The phone number to set.
        """
        self._phone = self._validate_phone(value)

    @property
    def description(self) -> Optional[str]:
        return self._description

    @description.setter
    def description(self, value: Optional[str]):
        self._description = value

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @created_at.setter
    def created_at(self, value: datetime):
        """
        Sets the created_at timestamp for the object.

        Args:
            value (datetime): The new timestamp to set as created_at.

        Raises:
            ValueError: If the provided value is later than the updated_at timestamp.
        """
        if hasattr(self, '_updated_at') and value > self._updated_at:
            raise ValueError("created_at cannot be later than updated_at.")
        if not isinstance(value, datetime):
            raise TypeError("created_at must be a datetime object.")
        self._created_at = value
        self._updated_at = value  # Initialize updated_at to created_at if not set
        self._created_at = value

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value: datetime):
        """
        Sets the updated_at timestamp for the object.

        Args:
            value (datetime): The new timestamp to set as updated_at.

        Raises:
            ValueError: If the provided value is earlier than the created_at timestamp.
        """
        if value < self._created_at:
            raise ValueError("updated_at cannot be earlier than created_at.")
        self._updated_at = value