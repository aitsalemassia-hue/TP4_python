from abc import ABC, abstractmethod


class Paiement(ABC):
     """Interface commune à tous les modes de paiement."""

     def __init__(self, montant: float):
          if montant <= 0:
               raise ValueError("Le montant doit être strictement positif")
          self._montant = montant

     @property
     def montant(self) -> float:
          return self._montant

     @abstractmethod
     def payer(self) -> str:
          """Retourne une chaîne de confirmation."""


class CarteBancaire(Paiement):

     def __init__(self, montant: float, numero: str, cvv: str):
          super().__init__(montant)
          numero = numero.replace(" ", "")
          if not self._luhn_valide(numero):
               raise ValueError("Numéro de carte invalide (16 chiffres, clé de Luhn)")
          if not (cvv.isdigit() and len(cvv) == 3):
               raise ValueError("Le CVV doit contenir 3 chiffres")
          self._numero = numero
          self._cvv = cvv

     @staticmethod
     def _luhn_valide(numero: str) -> bool:
          if not (numero.isdigit() and len(numero) == 16):
               return False
          total = 0
          for i, chiffre in enumerate(reversed(numero)):
               n = int(chiffre)
               if i % 2 == 1:      # un chiffre sur deux, en partant de la droite
                    n *= 2
                    if n > 9:
                         n -= 9
               total += n
          return total % 10 == 0

     def payer(self) -> str:
          return (f"Paiement de {self._montant} € effectué par carte bancaire "
                    f"(carte se terminant par {self._numero[-4:]}).")


class PayPal(Paiement):

     def __init__(self, montant: float, email: str, token: str):
          super().__init__(montant)
          if "@" not in email or "." not in email.split("@")[-1]:
               raise ValueError("Adresse e-mail invalide")
          if not token:
               raise ValueError("Le token d'API est obligatoire")
          self._email = email
          self._token = token

     def payer(self) -> str:
          return f"Paiement de {self._montant} DH effectué via PayPal (compte : {self._email})."


class Crypto(Paiement):
     RESEAUX = {"BTC", "ETH", "SOL", "LTC"}

     def __init__(self, montant: float, wallet_id: str, reseau: str):
          super().__init__(montant)
          if not wallet_id:
               raise ValueError("L'identifiant de portefeuille est obligatoire")
          if reseau.upper() not in self.RESEAUX:
               raise ValueError(f"Réseau inconnu (attendu : {sorted(self.RESEAUX)})")
          self._wallet_id = wallet_id
          self._reseau = reseau.upper()

     def payer(self) -> str:
          return (f"Paiement de {self._montant} DH effectué en crypto-monnaie "
                    f"(réseau {self._reseau}, portefeuille : {self._wallet_id}).")


def traiter_paiements(liste):
     """Polymorphisme : aucun isinstance, chaque objet sait payer()."""
     for paiement in liste:
          print(paiement.payer())


