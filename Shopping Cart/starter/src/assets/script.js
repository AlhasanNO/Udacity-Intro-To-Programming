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

function addProductToCart(productId) {
  const product = products.find(p => p.productId === productId);
  const cartItem = cart.find(item => item.productId === productId);
  if (cartItem) {
    cartItem.quantity += 1;
  } else {
    cart.push({ ...product, quantity: 1 });
  }
}

function increaseQuantity(productId) {
  const cartItem = cart.find(item => item.productId === productId);
  if (cartItem) {
    cartItem.quantity += 1;
  }
}

function decreaseQuantity(productId) {
  const cartItem = cart.find(item => item.productId === productId);
  if (cartItem) {
    cartItem.quantity -= 1;
    if (cartItem.quantity === 0) {
      removeProductFromCart(productId);
    }
  }
}

function removeProductFromCart(productId) {
  cart = cart.filter(item => item.productId !== productId);
}

function cartTotal() {
  return cart.reduce((total, item) => total + item.price * item.quantity, 0);
}

function emptyCart() {
  cart = [];
  totalPaid = 0;
}

function pay(amount) {
  totalPaid += amount;
  const total = cartTotal();
  return totalPaid - total;
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
