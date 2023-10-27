import ujson
from typing import List, Tuple

from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.service import NodeService
from uc_flow_nodes.views import info, execute
from uc_flow_schemas import flow
from uc_flow_schemas.flow import Property, CredentialProtocol, RunState
from uc_http_requester.requester import Request


class NodeType(flow.NodeType):
    id: str = '07042c7c-b34e-4337-8931-a8cf2504be6d'
    type: flow.NodeType.Type = flow.NodeType.Type.action
    name: str = 'RadiantBot'
    displayName: str = 'RadiantBot'
    icon: str = '<svg><text x="8" y="50" font-size="50">🤖</text></svg>'
    description: str = 'RadiantBot'
    properties: List[Property] = [
        Property(
            displayName='Тестовое поле',
            name='foo_field',
            type=Property.Type.JSON,
            placeholder='Foo placeholder',
            description='Foo description',
            required=True,
            default='Test data',
        ),
        Property(
            displayName='Текстовое поле',
            name='text_field',
            type=Property.Type.STRING,
            placeholder='Text',
            description='Текстовое поле',
            required=True,
            default='Test text',
        ),
        Property(
            displayName='Числовое поле',
            name='number_field',
            type=Property.Type.NUMBER,
            placeholder='Number',
            description='Числовое поле',
            required=True,
            default=0,
        ),
        Property(
            displayName='Тип значения',
            name='boolean_field',
            type=Property.Type.BOOLEAN,
            placeholder='Переключатель',
            description='Выкл - str, Вкл - number',
            required=True,
            default=False,
        )
    ]


class InfoView(info.Info):
    class Response(info.Info.Response):
        node_type: NodeType


class ExecuteView(execute.Execute):
    async def calculate(self, properties):
        result = int(properties['text_field']) + properties['number_field']
        return str(result) if not properties['boolean_field'] else result

    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            result = await self.calculate(json.node.data.properties)            
            await json.save_result({
                "result": result
            })
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
