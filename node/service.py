import ujson
from typing import Any, List, Tuple

from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.service import NodeService
from uc_flow_nodes.views import info, execute
from uc_flow_schemas import flow
from uc_flow_schemas.flow import Property, CredentialProtocol, RunState, OptionValue, DisplayOptions
from uc_http_requester.requester import Request
from node.credential_type import CredentialType
from node.enums import Resource

class NodeType(flow.NodeType):
    id: str = '002177ac-590c-44c9-bad9-b557934b97e5'
    type: flow.NodeType.Type = flow.NodeType.Type.action
    name: str = 'RadiantBotAuth'
    displayName: str = 'RadiantBotAuth'
    icon: str = '<svg><text x="0" y="50" font-size="50">👽</text></svg>'
    description: str = 'RadiantBotAuth'
    properties: List[Property] = []
    credentials: List[flow.NodeType.Credential] = [
        flow.NodeType.Credential(name="alfacrm_api_auth", required=True)
    ]

class InfoView(info.Info):
    class Response(info.Info.Response):
        node_type: NodeType
        credential_types: Tuple[CredentialType] = (CredentialType(),)


class ExecuteView(execute.Execute):

    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            credentials = await json.get_credentials()
            url = credentials.data.get('hostname')
            api_key = credentials.data.get('api_key')
            email = credentials.data.get('email')
            request = Request(
                url=f'https://{url}/v2api/auth/login',
                method=Request.Method.post,
                json={
                    "email": email,
                    "api_key": api_key
                }
            )
            result = await request.execute()
            await json.save_result(
                result.json()
            )
            json.state = RunState.complete
        except Exception as e:
            self.log.warning(f'Error {e}')
            await json.save_error(str(e))
            json.state = RunState.error
        return json


class Service(NodeService):
    class Routes(NodeService.Routes):
        Info = InfoView
        Execute = ExecuteView
