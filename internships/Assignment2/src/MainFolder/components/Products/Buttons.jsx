import * as React from 'react';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import FavoriteIcon from '@mui/icons-material/Favorite';
import ShoppingCartIcon from '@mui/icons-material/ShoppingCart';

export default function Buttons() {

  return (
    <Stack spacing={5} direction="row" sx={ {justifyContent:"center" ,alignContent:"center"}}>
      <Button variant="contained" sx={{backgroundColor:"#50a2a3"}}>Buy Now</Button>
      <Button variant="outlined" sx={{backgroundColor:"#50a2a3",color:"white"}}><ShoppingCartIcon sx={{backgroundColor:"#50a2a3"}}/>Add to Cart</Button>
    </Stack>
  );
}
