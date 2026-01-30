module.exports = {
    default: {
        input: {
            target: 'http://localhost:8000/openapi.json', // Where to fetch the OpenAPI spec
            filters: {
                tags: ['admin'],
            },
        },
        output: {
            target: './src/lib/api/gen', // Output directory for generated code
            schemas: './src/lib/api/gen/model', // Separate directory for TypeScript types
            client: 'axios', // Use axios for HTTP requests
            mode: 'split', // Generate separate files per endpoint
            clean: true, // Clean the output directory before generating
            baseUrl: 'http://localhost:8000', // Base URL for API requests
        },
    },
};