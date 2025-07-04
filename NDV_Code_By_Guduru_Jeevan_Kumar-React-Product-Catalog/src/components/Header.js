import React from 'react';

const Header = ({ children }) => (
  <header className="app-header">
    <div className="header-container header-inner">
      {children}
    </div>
  </header>
);

export default Header;
