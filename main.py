from datamodel import Order, Symbol, TradingState
from rounds.round_1.round import Trader as TraderRound1
from utils.logger import Logger

logger = Logger()


class Trader(TraderRound1):
    def run(self, state: TradingState) -> tuple[dict[Symbol, list[Order]], int, str]:
        result = super().run(state)
        logger.flush(state, *result)
        return result
