`transform` method in the LLE algorithm. This is not referenced from the article but implementation is straightforward:

   1. Compute barycenter coordinates for new points with respect to the trained data.
   2. Get the embedding vectors for these neighbors.
   3. multiply the embedding vectors by the barycenter weights.