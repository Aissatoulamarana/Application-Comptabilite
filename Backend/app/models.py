from django.db import models

# Create your models here.

# Modèle pour les utilisateurs

# Modèle pour les parametres societe

# Modèle pour les comptes du plan comptable
class Account(models.Model):
    code = models.CharField(max_length=10, unique=True, verbose_name="Code du compte")
    name = models.CharField(max_length=255, verbose_name="Nom du compte")
    ACCOUNT_TYPES = [
        ('actif', 'Actif', 'ACTIF'),
        ('passif', 'Passif', 'PASSIF'),
        ('produit', 'Produit', 'PRODUIT'),
        ('charge', 'Charge', 'CHARGE'),
        ('capitaux', 'Capitaux', 'CAPITAUX'),
    ]
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES, verbose_name="Type de compte")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dernière mise à jour")

    def __str__(self):
        return f"{self.code} - {self.name}"
    
# Modèle pour les tiers

# Modèle pour les codes journaux
     
# Modèle pour le journal 

# Modèle pour les ecritures comptables  

# Modèle pour les transactions
class Transaction(models.Model):
    date = models.DateField(verbose_name="Date de la transaction")
    description = models.TextField(verbose_name="Description", blank=True)
    debit_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='debits', verbose_name="Compte débit")
    credit_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='credits', verbose_name="Compte crédit")
    amount = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Montant")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")

    def __str__(self):
        return f"{self.date} - {self.amount} GNF"

# Modèle pour les factures
class Invoice(models.Model):
    number = models.CharField(max_length=20, unique=True, verbose_name="Numéro de facture")
    client_name = models.CharField(max_length=255, verbose_name="Nom du client")
    amount = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Montant total")
    date = models.DateField(verbose_name="Date de la facture")
    is_paid = models.BooleanField(default=False, verbose_name="Est payée")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")

    def __str__(self):
        return f"Facture {self.number} - {self.client_name}"
      