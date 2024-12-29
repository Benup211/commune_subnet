from communex.module import Module, endpoint
from communex.key import generate_keypair
from keylimiter import TokenBucketLimiter


class Miner(Module):
    @endpoint
    def generate(self, prompt: str, model: str = "foo"):
        print(f"Answering: `{prompt}` with model `{model}`")
        return {"answer": "Answered"}


if __name__ == "__main__":
    from communex.module.server import ModuleServer
    import uvicorn

    key = generate_keypair()
    miner = Miner()
    refill_rate = 1 / 400
    bucket = TokenBucketLimiter(2, refill_rate)
    server = ModuleServer(miner, key, ip_limiter=bucket,subnets_whitelist=[49])
    app = server.get_fastapi_app()

    uvicorn.run(app, host="127.0.0.1", port=8000)