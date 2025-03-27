# UiS-POP2-v2

A Next.js 14 application with AI integration capabilities, featuring OpenAI, Anthropic, and Google AI services.

## Features

- Next.js 14 App Router
- TypeScript
- Tailwind CSS
- Shadcn UI
- AI Integration (OpenAI, Anthropic, Google AI)
- Real-time data visualization
- Interactive data analysis
- Responsive design
- Dark mode support

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/ChineeWetto/UiS-POP2-v2.git
cd UiS-POP2-v2
```

2. Install dependencies:
```bash
pnpm install
```

3. Set up environment variables:
```bash
cp .env.example .env.local
```

4. Start the development server:
```bash
pnpm dev
```

5. Open [http://localhost:3000](http://localhost:3000) in your browser.

## Environment Variables

Create a `.env.local` file in the root directory and add the following variables:

```env
# OpenAI
OPENAI_API_KEY=your_openai_api_key

# Anthropic
ANTHROPIC_API_KEY=your_anthropic_api_key

# Google AI
GOOGLE_AI_API_KEY=your_google_ai_api_key

# Vercel KV (Optional)
KV_URL=your_kv_url
KV_REST_API_URL=your_kv_rest_api_url
KV_REST_API_TOKEN=your_kv_rest_api_token
KV_REST_API_READ_ONLY_TOKEN=your_kv_read_only_token
```

## Project Structure

```
.
├── app/                # Next.js app directory
│   ├── api/           # API routes
│   └── ...           # Page routes
├── components/        # React components
│   ├── ui/           # UI components
│   └── ...          # Feature components
├── lib/              # Utility functions
├── styles/           # Global styles
└── public/           # Static assets
```

## Contributing

1. Create a new branch for your feature:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes and commit them:
```bash
git commit -m "feat: add your feature"
```

3. Push to your branch:
```bash
git push origin feature/your-feature-name
```

4. Create a Pull Request on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

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

