# language: fr

@initial-release @login
Fonctionnalité: Identifier un utilisateur

  En tant qu'utilisateur enregistré dans le Shopozor,
  je veux pouvoir m'identifier avec un e-mail et un mot de passe
  afin de pouvoir faire mes achats ou accéder aux outils de gestion liés à mon compte.

  Les utilisateurs suivants sont des "clients":

  * Consommateur

  Les utilisateurs suivants sont des "administrateurs":

  * Producteur
  * Responsable
  * Rex
  * Softozor

  Contexte: L'utilisateur n'est pas identifié
    Etant donné un utilisateur non identifié sur le Shopozor

  Plan du Scénario: L'utilisateur n'est pas encore enregistré
    Lorsqu'un <utilisateur> s'identifie en tant que <utilisateur prétendu> avec un e-mail et un mot de passe invalides
    Alors il obtient un message d'erreur stipulant que ses identifiants sont incorrects

    Exemples:
      | utilisateur    | utilisateur prétendu |
      | client         | client               |
      | administrateur | client               |
      | client         | administrateur       |
      | administrateur | administrateur       |

  Plan du Scénario: L'utilisateur est enregistré mais entre un mot de passe erroné
    Lorsqu'un <utilisateur> s'identifie en tant que <utilisateur prétendu> avec un e-mail valide et un mot de passe invalide
    Alors il obtient un message d'erreur stipulant que ses identifiants sont incorrects

    Exemples:
      | utilisateur    | utilisateur prétendu |
      | client         | client               |
      | administrateur | client               |
      | client         | administrateur       |
      | administrateur | administrateur       |

  Plan du Scénario: L'utilisateur peut s'identifier avec son identifiant et son mot de passe

    La session s'ouvre avec les flags `httpOnly` et `secure`. N'importe quel administrateur peut s'identifier en tant que client.

    Lorsqu'un <utilisateur> s'identifie en tant que <utilisateur prétendu> avec un e-mail et un mot de passe valides
    Alors sa session sécurisée s'ouvre pour 1 mois

    Exemples:
      | utilisateur    | utilisateur prétendu |
      | client         | client               |
      | administrateur | administrateur       |
      | administrateur | client               |

  Scénario: Un client ne peut pas s'identifier en tant qu'administrateur
    Lorsqu'un client s'identifie en tant qu'administrateur avec un e-mail et un mot de passe valides
    Alors il obtient un message d'erreur stipulant que ses identifiants sont incorrects
