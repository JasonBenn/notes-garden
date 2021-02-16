import React from 'react';
import {Box} from 'theme-ui';

import ReferredBlock from 'gatsby-theme-andy/src/components/ReferredBlock';


const Footer = ({ references }) => {
  return (
    <Box p={3} sx={{ borderRadius: 2 }} mb={2} bg="accent" color="text-light">
      <ReferredBlock references={references} />
    </Box>
  );
};

export default Footer;
