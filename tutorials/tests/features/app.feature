Feature: Cadastrar tutoriais no admin do django

    Scenario: Como administrador do site
    Given Eu acesso a url /admin
    Then Eu faço login na pagina administrativa
    Then Eu acesso a app de tutoriais
    Then Eu cadastro um novo tutorial
