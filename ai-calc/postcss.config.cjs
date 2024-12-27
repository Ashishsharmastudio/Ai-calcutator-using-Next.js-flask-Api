const { Variable } = require("lucide-react");

module.exports = {
  plugins: {
    'postcss-present-mantine': {},
        'postcss-simple-vars': {
            Variables: {
                "mantine-breakpoint-xs": "36em",
                "mantine-breakpoint-sm": "48em",
                "mantine-breakpoint-md": "62em",
                "mantine-breakpoint-lg": "75em",
                "mantine-breakpoint-xl": "88em",
        }
    }  
  },
};