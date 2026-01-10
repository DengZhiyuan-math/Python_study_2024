import hashlib
import json
import time
from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Optional


def sha256_hex(data: str) -> str:
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def canonical_json(obj: Any) -> str:
    # 排序键、紧凑表示，保证同样内容序列化结果稳定
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


@dataclass(frozen=True)
class Block:
    index: int
    timestamp: float
    transactions: List[Dict[str, Any]]
    previous_hash: str
    nonce: int
    hash: str


class Blockchain:
    def __init__(self, difficulty: int = 4):
        if difficulty < 1 or difficulty > 10:
            raise ValueError("difficulty 建议 1~10（玩具实现）")
        self.difficulty = difficulty
        self.chain: List[Block] = []
        self.mempool: List[Dict[str, Any]] = []
        self._create_genesis_block()

    # ---------- 区块与哈希 ----------
    def _block_header_dict(
        self,
        index: int,
        timestamp: float,
        transactions: List[Dict[str, Any]],
        previous_hash: str,
        nonce: int,
    ) -> Dict[str, Any]:
        return {
            "index": index,
            "timestamp": timestamp,
            "transactions": transactions,
            "previous_hash": previous_hash,
            "nonce": nonce,
        }

    def _compute_hash(
        self,
        index: int,
        timestamp: float,
        transactions: List[Dict[str, Any]],
        previous_hash: str,
        nonce: int,
    ) -> str:
        header = self._block_header_dict(index, timestamp, transactions, previous_hash, nonce)
        return sha256_hex(canonical_json(header))

    def _is_valid_pow(self, block_hash: str) -> bool:
        return block_hash.startswith("0" * self.difficulty)

    # ---------- 创世块 ----------
    def _create_genesis_block(self) -> None:
        # 创世块通常固定写死。这里也用 PoW 挖一下，保持一致性。
        genesis = self._mine_block(transactions=[{"from": "genesis", "to": "genesis", "amount": 0}], previous_hash="0")
        self.chain.append(genesis)

    # ---------- 交易 ----------
    def add_transaction(self, sender: str, recipient: str, amount: float) -> int:
        if amount <= 0:
            raise ValueError("amount 必须为正数")
        tx = {"from": sender, "to": recipient, "amount": amount, "ts": time.time()}
        self.mempool.append(tx)
        return len(self.mempool)  # 返回交易池大小（仅做演示）

    # ---------- 挖矿（PoW） ----------
    def mine_pending_transactions(self) -> Block:
        if not self.mempool:
            raise RuntimeError("没有待打包交易")
        previous_hash = self.chain[-1].hash
        block = self._mine_block(transactions=self.mempool, previous_hash=previous_hash)
        self.chain.append(block)
        self.mempool = []
        return block

    def _mine_block(self, transactions: List[Dict[str, Any]], previous_hash: str) -> Block:
        index = len(self.chain)
        timestamp = time.time()
        nonce = 0

        while True:
            h = self._compute_hash(index, timestamp, transactions, previous_hash, nonce)
            if self._is_valid_pow(h):
                return Block(
                    index=index,
                    timestamp=timestamp,
                    transactions=transactions,
                    previous_hash=previous_hash,
                    nonce=nonce,
                    hash=h,
                )
            nonce += 1

    # ---------- 校验 ----------
    def is_chain_valid(self, chain: Optional[List[Block]] = None) -> bool:
        chain = chain or self.chain
        if not chain:
            return False

        # 检查创世块 PoW/哈希自洽（previous_hash 可放宽，这里简化）
        for i in range(len(chain)):
            b = chain[i]
            # 1) 哈希必须等于重新计算结果
            recomputed = self._compute_hash(
                b.index, b.timestamp, b.transactions, b.previous_hash, b.nonce
            )
            if b.hash != recomputed:
                return False

            # 2) PoW 必须满足难度
            if not self._is_valid_pow(b.hash):
                return False

            # 3) previous_hash 必须串起来
            if i > 0 and b.previous_hash != chain[i - 1].hash:
                return False

            # 4) index 连续（玩具要求）
            if b.index != i:
                return False

        return True

    # ---------- 最长链原则（玩具版） ----------
    def replace_chain_if_longer(self, candidate_chain: List[Block]) -> bool:
        """
        真实网络里会从邻居节点拉取链，这里只提供接口：
        - 候选链更长
        - 候选链有效
        则替换
        """
        if len(candidate_chain) <= len(self.chain):
            return False
        if not self.is_chain_valid(candidate_chain):
            return False
        self.chain = candidate_chain
        return True

    # ---------- 工具 ----------
    def to_json(self) -> str:
        return canonical_json([asdict(b) for b in self.chain])


if __name__ == "__main__":
    bc = Blockchain(difficulty=4)

    bc.add_transaction("alice", "bob", 5)
    bc.add_transaction("bob", "carol", 2)
    mined = bc.mine_pending_transactions()
    print("Mined block:", mined.index, mined.hash, "nonce=", mined.nonce)

    bc.add_transaction("carol", "deng", 1.5)
    mined2 = bc.mine_pending_transactions()
    print("Mined block:", mined2.index, mined2.hash, "nonce=", mined2.nonce)

    print("Chain valid?", bc.is_chain_valid())
    print("Chain length:", len(bc.chain))
    print("Chain json:", bc.to_json()[:200], "...")
