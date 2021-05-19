from fastapi import APIRouter,WebSocket,WebSocketDisconnect

socks=APIRouter()

current_num=[0]


@socks.websocket("/join")
async def joining_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            if data == 'addone':
                current_num
                result=current_num[-1]+1
                current_num.append(result)    
                await websocket.send_text(str(current_num[-1]))
            elif data == 'get_current':
                await websocket.send_text(str(current_num[-1]))
            else:
                pass
    except WebSocketDisconnect:
        pass