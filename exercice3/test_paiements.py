from paiements import CarteBancaire, PayPal, Crypto, traiter_paiements

if __name__ == "__main__":
     paiement_carte = CarteBancaire(100, "1234 5678 9012 3456", "123")
     paiement_paypal = PayPal(200, "assiya@example.com", "tok_abc123")
     paiement_crypto = Crypto(150, "0xA1B2C3D4", "Ethereum")

     paiements = [paiement_carte, paiement_paypal, paiement_crypto]

     for paiement in paiements:
          print(paiement.payer())
          print(f"Montant: {paiement.montant}")

     traiter_paiements(paiements)