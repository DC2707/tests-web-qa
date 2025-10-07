describe('Checkout flow with slow payment response', () => {
  it('handles slow payment endpoint gracefully', () => {
    cy.visit('/')
    cy.get('.search_query').type('dress{enter}')
    cy.get('.product_img_link').first().click()
    cy.get('#add_to_cart button').click()
    cy.get("a[title='Proceed to checkout']").click()

    cy.intercept('POST', '/order', (req) => {
      req.reply((res) => {
        res.setDelay(5000)
        res.send({ statusCode: 500, body: { error: "simulated payment error" } })
      })
    }).as('payment')
  })
})
