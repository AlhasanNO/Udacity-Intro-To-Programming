let cart = [];
let totalPaid = 0;

const products = [
  {
    name: "Cherry",
    price: 1.50,
    quantity: 0,
    productId: 100,
    image: "images/cherry.jpg"
  },
  {
    name: "Orange",
    price: 2.00,
    quantity: 0,
    productId: 101,
    image: "images/orange.jpg"
  },
  {
    name: "Strawberry",
    price: 3.00,
    quantity: 0,
    productId: 102,
    image: "images/strawberry.jpg"
  }
];

// Function to find a product by its productId
function findProductById(productId) {
  return products.find(p => p.productId === productId);
}

// Function to find an item in the cart by its productId
function findCartItemById(productId) {
  return cart.find(item => item.productId === productId);
}

// Function to add a product to the cart
function addProductToCart(productId) {
  const product = findProductById(productId);
  const cartItem = findCartItemById(productId);

  if (cartItem) {
    // If the product is already in the cart, increase its quantity
    cartItem.quantity += 1;
  } else {
    // If the product is not in the cart, add it with a quantity of 1
    product.quantity = 1;
    cart.push(product);
  }
}

// Function to increase the quantity of a product in the cart
function increaseQuantity(productId) {
  const cartItem = findCartItemById(productId);
  if (cartItem) {
    // Increase the quantity by 1
    cartItem.quantity += 1;
  }
}

// Function to decrease the quantity of a product in the cart
function decreaseQuantity(productId) {
  const cartItem = findCartItemById(productId);
  if (cartItem) {
    // Decrease the quantity by 1
    cartItem.quantity -= 1;
    if (cartItem.quantity === 0) {
      // If the quantity reaches 0, remove the product from the cart
      removeProductFromCart(productId);
    }
  }
}

// Function to remove a product from the cart
function removeProductFromCart(productId) {
  const product = findCartItemById(productId);

  if (product) {
    cart.splice(cart.indexOf(product), 1);
  }
}

// Helper function to calculate the total cost of the cart
function calculateCartTotal(cart) {
  return cart.reduce((total, item) => total + item.price * item.quantity, 0);
}

// Function to calculate the total cost of all items in the cart
function cartTotal() {
  return calculateCartTotal(cart);
}

// Function to empty the cart and reset the totalPaid amount
function emptyCart() {
  cart.forEach(item => {
    const product = findCartItemById(productId);
    if (product) {
      product.quantity += item.quantity;
    }
  });

  cart = [];
}

// Function to handle payment
function pay(amount) {
  const total = cartTotal();

  // If the amount paid is less than the cart total, return the amount still owed (negative)
  if (amount < total) {
    const amountStillOwed = amount - total;
    console.error(`Payment failed: Amount paid is less than the cart total. Amount still owed: ${-amountStillOwed}`);
    return amountStillOwed;
  }

  totalPaid += amount;
  const remainingBalance = totalPaid - total;

  // If the remaining balance is positive or zero, reset totalPaid and empty the cart
  if (remainingBalance >= 0) {
    totalPaid = 0;
    emptyCart();
  }

  return remainingBalance;
}

/* Place stand out suggestions here (stand out suggestions can be found at the bottom of the project rubric.)*/


/* The following is for running unit tests. 
   To fully complete this project, it is expected that all tests pass.
   Run the following command in terminal to run tests
   npm run test
*/

module.exports = {
  products,
  cart,
  addProductToCart,
  increaseQuantity,
  decreaseQuantity,
  removeProductFromCart,
  cartTotal,
  pay,
  emptyCart,
  /* Uncomment the following line if completing the currency converter bonus */
  // currency
}
