Feature: Cadastrar palestras no admin do django

    Scenario: Como administrador do site
    Given Eu acesso a url /admin
    Then Eu faço login na pagina administrativa
    Then Eu acesso a app de palestras
    Then Eu cadastro um novo palestra
