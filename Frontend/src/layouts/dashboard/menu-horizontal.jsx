import { useState } from 'react';

import Box from '@mui/material/Box';
import Menu from '@mui/material/Menu';
import Button from '@mui/material/Button';
import MenuItem from '@mui/material/MenuItem';

export function HorizontalMenu() {
  const [menuAnchor, setMenuAnchor] = useState(null);
  const [activeMenu, setActiveMenu] = useState('');

  const handleMenuOpen = (event, menu) => {
    setMenuAnchor(event.currentTarget);
    setActiveMenu(menu);
  };

  const handleMenuClose = () => {
    setMenuAnchor(null);
    setActiveMenu('');
  };

  const menuItems = {
    Fichier: ['Nouveau', 'Ouvrir', 'Enregistrer', 'Quitter'],
    Édition: ['Annuler', 'Répéter', 'Copier', 'Coller'],
    Structure: ['Ajouter', 'Supprimer', 'Modifier'],
    Traitement: ['Lancer', 'Arrêter', 'Reprendre'],
    État: ['Rapport', 'Statistiques'],
    Fenêtre: ['Cascade', 'Mosaïque', 'Fermer tout'],
  };

  return (
    <Box display="flex" gap={2}>
      {Object.keys(menuItems).map((menu) => (
        <Box key={menu}>
          <Button onClick={(e) => handleMenuOpen(e, menu)}>{menu}</Button>
          <Menu
            anchorEl={menuAnchor}
            open={Boolean(menuAnchor) && activeMenu === menu}
            onClose={handleMenuClose}
          >
            {menuItems[menu]?.map((item) => (
              <MenuItem key={item} onClick={handleMenuClose}>
                {item}
              </MenuItem>
            ))}
          </Menu>
        </Box>
      ))}
    </Box>
  );
}
