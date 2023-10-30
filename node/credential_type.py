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
    # properties: List[Property] = [
    #     Property(
    #         displayName='URL',
    #         name='base_url',
    #         type=Property.Type.STRING,
    #         default='',
    #     ),
    #     Property(
    #         displayName='API key',
    #         name='auth.token',
    #         type=Property.Type.STRING,
    #         default='',
    #     ),
    # ]
    extends: Optional[List[str]] = []
    # icon: Optional[str] = ICON
