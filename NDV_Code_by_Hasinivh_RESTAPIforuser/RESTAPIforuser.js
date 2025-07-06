const express = require('express');
const mongoose = require('mongoose');

const app = express();
app.use(express.json()); // Built-in body parser

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/shopDB')
  .then(() => console.log('Connected to MongoDB'))
  .catch(err => console.error(err));

// User Model
const User = mongoose.model('User', {
  name: String,
  email: String
});

// Product Model
const Product = mongoose.model('Product', {
  name: String,
  price: Number
});

// User Routes
app.post('/users', async (req, res) => res.send(await new User(req.body).save()));
app.get('/users', async (req, res) => res.send(await User.find()));
app.put('/users/:id', async (req, res) => res.send(await User.findByIdAndUpdate(req.params.id, req.body, { new: true })));
app.delete('/users/:id', async (req, res) => res.send(await User.findByIdAndDelete(req.params.id)));

// Product Routes
app.post('/products', async (req, res) => res.send(await new Product(req.body).save()));
app.get('/products', async (req, res) => res.send(await Product.find()));
app.put('/products/:id', async (req, res) => res.send(await Product.findByIdAndUpdate(req.params.id, req.body, { new: true })));
app.delete('/products/:id', async (req, res) => res.send(await Product.findByIdAndDelete(req.params.id)));

// Start Server
app.listen(3000, () => console.log('API running on http://localhost:3000'));
