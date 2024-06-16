from entities.dao.abstractDAO import AbstractDAO
from entities.affiliate import Affiliate


class AffiliateDAO(AbstractDAO):
    def __init__(self):
        super().__init__("pkl/affiliates.pkl")
