import React from 'react';
import {Link} from 'gatsby';
import {Box, Styled} from 'theme-ui';

export default ({ siteMetadata }) => (
  <header>
    <Box py={2} px={3} sx={{ borderBottom: '1px solid', borderColor: 'gray', backgroundColor: "white", display: "flex", justifyContent: "space-between", fontSize: "17px" }}>
      <Link to="/" style={{ fontWeight: '500', color: '#333', textDecoration: 'none' }}>
        {siteMetadata.title}
      </Link>

      <span style={{color: "rgb(183 183 183)"}}>
        Care to comment? Message me on{' '}
        <Link
          style={{ textDecoration: 'underline', color: 'inherit' }}
          href="https://twitter.com/messages/compose?recipient_id=953904672"
        >
          Twitter
        </Link>{' '}
        or{' '}
        <Link style={{ textDecoration: 'underline', color: 'inherit' }} href="mailto:jasoncbenn+notes@gmail.com">
          email
        </Link>{' '}
        me.
      </span>

    </Box>

  </header>
);
