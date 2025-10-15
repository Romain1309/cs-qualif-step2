from fastapi import Request, status
from fastapi.responses import JSONResponse
from cs_qualif_step2.core.domain.exception.unsupported_value_exception import UnsupportedValueException

async def unsupported_value_exception_handler(request: Request, exc: UnsupportedValueException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"error": exc.message}
    )