from django.db import models
from django.contrib.auth.models import AbstractUser
from decimal import Decimal
from django.utils import timezone



# Create your models here.

# Modèle pour les utilisateurs
class CustomUser(AbstractUser):
    # Ajouter des champs personnalisés si nécessaire
    ROLE_CHOICES = [
        ('admin', 'Administrateur'),
        ('comptable', 'Comptable'),
        ('user', 'Utilisateur'),
    ]
    role = models.CharField(
        max_length=20, 
        choices=ROLE_CHOICES, 
        default='user', 
        verbose_name="Rôle"
    )
    phone_number = models.CharField(
        max_length=15, 
        blank=True, 
        null=True, 
        verbose_name="Numéro de téléphone"
    )
    
    def __str__(self):
        return f"{self.username} ({self.role})"
    



# Modèle pour les parametres societe
class CompanySettings(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nom de la société")
    address = models.TextField(verbose_name="Adresse")
    phone = models.CharField(max_length=20, verbose_name="Téléphone")
    email = models.EmailField(verbose_name="Email")
    tax_number = models.CharField(
        max_length=50, 
        verbose_name="Numéro d'identification fiscale",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Dernière mise à jour")

    def __str__(self):
        return self.name
    



# Modèle pour les comptes du plan comptable
class Compte(models.Model):
    # Type de compte selon le plan comptable
    type_choices = [
        ('1', 'Actif'),
        ('2', 'Passif'),
        ('3', 'Capitaux propres'),
        ('4', 'Produits'),
        ('5', 'Charges'),
    ]

    numero = models.CharField(max_length=10, unique=True, verbose_name="Numéro du compte")
    libelle = models.CharField(max_length=255, verbose_name="Libellé du compte")
    type_compte = models.CharField(max_length=1, choices=type_choices, verbose_name="Type de compte")
    solde_initial = models.DecimalField(max_digits=15, decimal_places=2, default=0.00, verbose_name="Solde initial")
    solde_actuel = models.DecimalField(max_digits=15, decimal_places=2, default=0.00, verbose_name="Solde actuel")
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")

    def __str__(self):
        return f"{self.numero} - {self.libelle}"

    class Meta:
        verbose_name = "Compte"
        verbose_name_plural = "Comptes"
        ordering = ['numero']
    


    
# Modèle pour les tiers
class Tier(models.Model):
    TYPE_CHOICES = [
        ('client', 'Client'),
        ('fournisseur', 'Fournisseur'),
        ('autre', 'Autre'),
    ]

    nom = models.CharField(max_length=255, verbose_name="Nom du tiers")
    adresse = models.TextField(blank=True, null=True, verbose_name="Adresse")
    telephone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Téléphone")
    email = models.EmailField(blank=True, null=True, verbose_name="Adresse Email")
    type_tier = models.CharField(max_length=20, choices=TYPE_CHOICES, default='autre', verbose_name="Type de tiers")
    numero_identification = models.CharField(max_length=50, blank=True, null=True, verbose_name="Numéro d'identification fiscale")
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")

    def __str__(self):
        return f"{self.nom} ({self.get_type_tier_display()})"

    class Meta:
        verbose_name = "Tier"
        verbose_name_plural = "Tiers"
        ordering = ['nom']




# Modèle pour les codes journaux
class CodeJournal(models.Model):
    # Définir les choix avant de les utiliser dans le modèle
    JOURNAL_CHOICES = [
        ('CAIS', 'Caisse'),
        ('BANQ', 'Banque'),
        ('VEND', 'Ventes'),
        ('ACHAT', 'Achats'),
        # Ajoutez d'autres choix ici
    ]
    
    TYPE_CHOICES = [
    ('A', 'Actif'),
    ('P', 'Passif'),
    ('R', 'Résultat'),
    # Ajoutez d'autres types ici
    ]

    code_journal = models.CharField(max_length=10, choices=JOURNAL_CHOICES, verbose_name="Code du journal")
    libelle = models.CharField(max_length=100, verbose_name="Libellé du journal")
    type_compte = models.CharField(max_length=1, choices=TYPE_CHOICES, verbose_name="Type de compte")
    date_creation = models.DateTimeField(default=timezone.now, verbose_name="Date de création")
    
    def __str__(self):
        return f"{self.code_journal} - {self.libelle}"

    class Meta:
        verbose_name = "Code Journal"
        verbose_name_plural = "Codes Journaux"




# Modèle pour le journal 
class Journal(models.Model):
    code_journal = models.ForeignKey(CodeJournal, on_delete=models.CASCADE, verbose_name="Code Journal", related_name="journaux")
    date_operation = models.DateField(verbose_name="Date de l'opération")
    reference = models.CharField(max_length=50, verbose_name="Référence de l'opération")
    libelle = models.CharField(max_length=255, verbose_name="Libellé de l'opération")
    montant_debit = models.DecimalField(max_digits=15, decimal_places=2, default=0.00, verbose_name="Montant Débit")
    montant_credit = models.DecimalField(max_digits=15, decimal_places=2, default=0.00, verbose_name="Montant Crédit")
    date_saisie = models.DateTimeField(auto_now_add=True, verbose_name="Date de saisie")

    def __str__(self):
        return f"{self.reference} - {self.libelle} ({self.date_operation})"

    class Meta:
        verbose_name = "Journal"
        verbose_name_plural = "Journaux"
        ordering = ['date_operation', 'reference']
        


# Modèle pour les ecritures comptables  
class EcritureComptable(models.Model):
    JOURNAL_TYPES = [
        ('D', 'Débit'),
        ('C', 'Crédit'),
    ]

    journal = models.ForeignKey('Journal', on_delete=models.CASCADE, verbose_name="Journal associé", related_name="ecritures")
    date_ecriture = models.DateField(verbose_name="Date de l'écriture")
    compte = models.CharField(max_length=20, verbose_name="Compte comptable")
    libelle = models.CharField(max_length=255, verbose_name="Libellé de l'écriture")
    type = models.CharField(max_length=1, choices=JOURNAL_TYPES, verbose_name="Type (Débit/Crédit)")
    montant = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Montant", default=Decimal('0.00'))
    reference = models.CharField(max_length=50, verbose_name="Référence de l'écriture", blank=True, null=True)

    def __str__(self):
        return f"{self.libelle} - {self.montant} {self.get_type_display()}"

    class Meta:
        verbose_name = "Écriture Comptable"
        verbose_name_plural = "Écritures Comptables"
        ordering = ['date_ecriture', 'journal']




# Modèle pour les transactions
class Transaction(models.Model):
    reference = models.CharField(max_length=50, unique=True, verbose_name="Référence de la transaction")
    date_transaction = models.DateField(verbose_name="Date de la transaction")
    libelle = models.CharField(max_length=255, verbose_name="Description de la transaction")
    montant_total = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Montant total")
    ecritures = models.ManyToManyField(EcritureComptable, related_name="transactions", verbose_name="Écritures associées")
    date_saisie = models.DateTimeField(auto_now_add=True, verbose_name="Date de saisie")

    def __str__(self):
        return f"Transaction {self.reference} - {self.libelle} ({self.montant_total})"

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"
        ordering = ['date_transaction', 'reference']


# Modèle pour les factures  
class Facture(models.Model):
    statut_choices = [
        ('E', 'En cours'),
        ('P', 'Payée'),
        ('A', 'Annulée'),
    ]
    
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name="factures")
    numero_facture = models.CharField(max_length=20, unique=True, verbose_name="Numéro de la facture")
    date_emission = models.DateField(verbose_name="Date d'émission")
    date_echeance = models.DateField(verbose_name="Date d'échéance")
    montant_total = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Montant total", default=Decimal('0.00'))
    statut = models.CharField(max_length=1, choices=statut_choices, default='E', verbose_name="Statut de la facture")
    libelle = models.CharField(max_length=255, verbose_name="Description de la facture")
    ecritures = models.ManyToManyField('EcritureComptable', related_name='factures', blank=True, verbose_name="Écritures comptables liées")
    date_saisie = models.DateTimeField(auto_now_add=True, verbose_name="Date de saisie")

    def __str__(self):
        return f"Facture {self.numero_facture} - {self.client.nom}"

    def montant_hors_taxe(self):
        """Calculer le montant hors taxe si applicable"""
        # Si vous avez des informations fiscales comme la TVA
        return self.montant_total / Decimal(1.2)  # Exemple pour une TVA de 20%

    class Meta:
        verbose_name = "Facture"
        verbose_name_plural = "Factures"
        ordering = ['date_emission', 'numero_facture']

class Client(models.Model):
    nom = models.CharField(max_length=255, verbose_name="Nom du client")
    adresse = models.CharField(max_length=255, verbose_name="Adresse du client", blank=True, null=True)
    email = models.EmailField(max_length=254, verbose_name="Email du client", blank=True, null=True)
    telephone = models.CharField(max_length=15, verbose_name="Numéro de téléphone", blank=True, null=True)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

