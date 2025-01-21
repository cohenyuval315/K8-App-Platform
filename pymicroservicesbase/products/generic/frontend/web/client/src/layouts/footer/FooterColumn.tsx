import React from 'react';

interface NavLink {
  name: string;
  href: string;
  children: NavLink[];
}

interface FooterColumnProps {
  // title: string;
  link: NavLink;
}

const FooterColumn: React.FC<FooterColumnProps> = ({ link }) => {
  const styles = {
    container: {
      padding: '20px',
      margin: '10px',
      backgroundColor: '#2b2b2b', // Darker background for contrast
      color: 'white',
      borderRadius: '12px',
      boxShadow: '0 4px 20px rgba(0, 0, 0, 0.3)',
      transition: 'transform 0.2s, box-shadow 0.2s',
    },
    title: {
      fontSize: '1.2rem',
      fontWeight: 'bold',
      marginBottom: '15px',
      // borderBottom: '2px solid #444', // Darker bottom border
      paddingBottom: '8px',
    },
    divider: {
      height: '2px',
      backgroundColor: '#555', // Thicker divider
      margin: '10px 0',
      border: 'none',
    },
    list: {
      listStyleType: 'none',
      padding: 0,
    },
    item: {
      margin: '10px 0', // Increased spacing between items
    },
    link: {
      color: '#66b3ff', // Bright link color
      textDecoration: 'none',
      fontSize: '1rem', // Slightly larger font for links
      transition: 'color 0.3s, transform 0.3s',
    },
    linkHover: {
      color: '#99ccff', // Lighter hover color
      transform: 'scale(1.05)', // Slightly larger on hover
    },
  };

  return (
    <div
      style={styles.container}
      onMouseEnter={(e) => {
        e.currentTarget.style.transform = 'scale(1.05)';
        e.currentTarget.style.boxShadow = '0 6px 30px rgba(0, 0, 0, 0.4)'; // Deeper shadow on hover
      }}
      onMouseLeave={(e) => {
        e.currentTarget.style.transform = 'scale(1)';
        e.currentTarget.style.boxShadow = '0 4px 20px rgba(0, 0, 0, 0.3)'; // Reset shadow
      }}
    >
      <label style={styles.title}>{link.name}</label>

      {link.children.length > 0 && (
        <>
          <hr style={styles.divider} />
          <ul style={styles.list}>
            {link.children.map((childLink) => (
              <li key={childLink.href} style={styles.item}>
                <a
                  href={childLink.href}
                  style={styles.link}
                  onMouseEnter={(e) => {
                    e.currentTarget.style.color = styles.linkHover.color;
                    e.currentTarget.style.transform = styles.linkHover.transform;
                  }}
                  onMouseLeave={(e) => {
                    e.currentTarget.style.color = styles.link.color;
                    e.currentTarget.style.transform = 'none';
                  }}
                >
                  {childLink.name}
                </a>
              </li>
            ))}
          </ul>
        </>
      )}
    </div>
  );
};

export default FooterColumn;
