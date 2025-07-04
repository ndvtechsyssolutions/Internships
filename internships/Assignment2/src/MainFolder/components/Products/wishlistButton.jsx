import Button from '@mui/material/Button';
import FavoriteIcon from '@mui/icons-material/Favorite';
import { Box } from '@mui/material';

function WishlistButton() {
  function addtoWishlist() {
    alert("hey you clicked me!");
  }

  return (
    <Box className="wishlist-button">
      <Button
        variant="contained"
        onClick={addtoWishlist}
        sx={{ backgroundColor: "white" }}
      >
        <FavoriteIcon sx={{ backgroundColor: 'blue' }} />
      </Button>
    </Box>
  );
}

export default WishlistButton;