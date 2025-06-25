import React from 'react';

const Footer = () => (
  <footer style={{ background: '#333', color: '#fff', padding: '12px 0', textAlign: 'center', marginTop: 40 }}>
    <p style={{ margin: 0 }}>&copy; {new Date().getFullYear()} Product Catalog. All rights reserved.</p>
  </footer>
);

export default Footer;
