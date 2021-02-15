import React from 'react';
import {Box, Styled} from 'theme-ui';

import ReferredBlock from 'gatsby-theme-andy/src/components/ReferredBlock';


const Footer = ({ references }) => {
  return (
    <Box p={3} sx={{ borderRadius: 2 }} mb={2} bg="accent" color="text-light">
      <ReferredBlock references={references} />
      <p sx={{ m: 0, fontSize: 1 }}>
        Care to comment? Message me on{' '}
        <Styled.a
          sx={{ textDecoration: 'underline', color: 'text-light' }}
          href="https://twitter.com/messages/compose?recipient_id=953904672"
        >
          Twitter
        </Styled.a>{' '}
        or{' '}
        <Styled.a sx={{ textDecoration: 'underline', color: 'text-light' }} href="mailto:jasoncbenn+notes@gmail.com">
          email
        </Styled.a>{' '}
        me.
      </p>
    </Box>
  );
};

export default Footer;
