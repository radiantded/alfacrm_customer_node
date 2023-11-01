from typing import List, Optional

from uc_flow_schemas import flow
from uc_flow_schemas.flow import (
    Property,
    CredentialProtocol,
)


class CredentialType(flow.CredentialType):
    id: str = 'alfacrm_api_auth'
    is_public: bool = True
    displayName: str = 'AlfaCRM API Auth'
    protocol: CredentialProtocol = CredentialProtocol.ApiKey
    protected_properties: List[Property] = []
    extends: Optional[List[str]] = []
