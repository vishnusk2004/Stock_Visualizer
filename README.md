---

# Stock Visualizer

This project aims to provide visualizations of stock data using AI-generated images. The visualizations include representations of cash stacks, office sizes, and comparisons between companies based on their financial data.

## Features

- Extract financial data from text for stocks with ticker symbols.
- Use AI to visualize:
  - Industry
  - Employee count
  - Quarterly profit
- Generate real-life images of:
  - Cash stacks representing quarterly profit
  - Office sizes comparing employee count
- Compare companies' visualizations
- Web application to display and compare the generated images

## Project Structure

- `server.py`: Flask server to serve the generated images.
- `src/ImageGallery.js`: React component to display the generated images.
- `src/App.js`: Main React application file.

## Setup

## Requirements

```sh
pip install -r requirements.txt
```

### Backend

1. **Install Flask:**

   ```sh
   pip install Flask
   ```

2. **Run the Flask Server:**

   ```sh
   python server.py
   ```

### Frontend

1. **Create a React Application:**

   ```sh
   npx create-react-app stock-visualizer
   cd stock-visualizer
   ```

2. **Install Axios:**

   ```sh
   npm install axios
   ```

3. **Run the React Application:**

   ```sh
   npm start
   ```

## Usage

1. **Start the Flask server:**

   ```sh
   python server.py
   ```

2. **Start the React application:**

   ```sh
   cd stock-visualizer
   npm start
   ```

3. Open your web browser and go to `http://localhost:3000` to see the generated images.

## License

This project is licensed under the MIT License.

---
