# UiS-POP2-v2

## Development Setup

### Prerequisites

- Node.js version 18.17.0 or higher
- pnpm version 10.x
- Git

### Environment Setup

1. Clone the repository:
```bash
git clone https://github.com/ChineeWetto/UiS-POP2-v2.git
cd UiS-POP2-v2
```

2. Install dependencies:
```bash
pnpm install
```

3. Create a `.env` file based on `.env.example`:
```bash
cp .env.example .env
```

4. Start the development server:
```bash
pnpm dev
```

### Build

To create a production build:
```bash
pnpm build
```

### Deployment

This project is configured for deployment on Vercel. The following environment variables are required:

- `NEXT_PUBLIC_API_URL`: API endpoint URL
- Add any other required environment variables here

### Project Structure

- `/app`: Next.js 14 app directory
- `/components`: React components
- `/lib`: Utility functions and shared code
- `/styles`: Global styles and Tailwind CSS configuration

### Technologies Used

- Next.js 14.1.3
- React 18
- TypeScript
- Tailwind CSS
- shadcn/ui components

## Contributing

1. Create a new branch for your feature
2. Make your changes
3. Submit a pull request

## License

MIT

# POP2 Research Project Website

This is the website for our undergraduate research project on human POP2 protein expression in E. coli and yeast systems.

## Adding Your Own Content

### Data Files

1. Place your data files in the `public/data/files` directory:
   - CSV files for expression data
   - PDF files for documentation
   - PDB files for protein structures
   - Any other relevant files

2. The files will be accessible at `/data/files/your-file-name.extension`

### Images

1. Place your images in the `public/images` directory
2. Reference them in your code as `/images/your-image.jpg`

### Interactive Data

1. Update the data in the API routes:
   - `app/api/expression-kinetics/route.ts`
   - `app/api/temperature-effects/route.ts`

2. Or modify the components to load data from your CSV files:
   - `components/data-visualization/expression-kinetics-chart.tsx`
   - `components/data-visualization/temperature-effects-chart.tsx`

### PyMOL Structure

1. Place your PDB file in `public/data/files/`
2. Update the `protein-structure-viewer.tsx` component to load your file:
   ```typescript
   // Change this line
   const structure = await stage.loadFile('/data/files/your-structure.pdb')

