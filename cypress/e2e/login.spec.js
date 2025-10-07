describe('Login flow', () => {
  it('logs in with valid creds', () => {
    cy.visit('/index.php?controller=authentication&back=my-account')
    cy.get('#email').type('test@example.com')
    cy.get('#passwd').type('password123')
    cy.get('#SubmitLogin').click()
    cy.contains('Authentication').should('exist')
  })
})
