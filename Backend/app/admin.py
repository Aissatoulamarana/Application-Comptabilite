from django.contrib import admin
from django.contrib import admin
from .models import CodeJournal

# Register your models here.
from .models import CustomUser, CompanySettings, Compte, Facture, Client, Tier, CodeJournal, Journal, EcritureComptable, Transaction

admin.site.register(CustomUser)
admin.site.register(CompanySettings)

@admin.register(Compte)
class CompteAdmin(admin.ModelAdmin):
    list_display = ('numero', 'libelle', 'type_compte', 'solde_initial', 'solde_actuel')
    search_fields = ('numero', 'libelle')
    list_filter = ('type_compte',)

@admin.register(Facture)
class FactureAdmin(admin.ModelAdmin):
    list_display = ('numero_facture', 'client', 'date_emission', 'montant_total', 'statut', 'date_saisie')
    search_fields = ('numero_facture', 'client__nom')
    list_filter = ('statut', 'date_emission', 'client')
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'telephone')
    search_fields = ('nom', 'email')
@admin.register(Tier)
class TierAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type_tier', 'telephone', 'email', 'date_creation')
    search_fields = ('nom', 'type_tier', 'email')
    list_filter = ('type_tier',)
@admin.register(CodeJournal)
class CodeJournalAdmin(admin.ModelAdmin):
    list_display = ('code_journal', 'libelle', 'type_compte', 'date_creation')  
    list_filter = ('type_compte',)
@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('reference', 'libelle', 'code_journal', 'date_operation', 'montant_debit', 'montant_credit', 'date_saisie')
    search_fields = ('reference', 'libelle', 'code_journal__code')
    list_filter = ('code_journal', 'date_operation')
@admin.register(EcritureComptable)
class EcritureComptableAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'journal', 'type', 'montant', 'date_ecriture')
    search_fields = ('libelle', 'compte', 'journal__code')
    list_filter = ('type', 'journal')
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('reference', 'libelle', 'montant_total', 'date_transaction')
    search_fields = ('reference', 'libelle')
    list_filter = ('date_transaction',)