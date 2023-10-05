import os
from unittest import TestCase
import numpy as np
import numpy.testing as nt
import uxarray as ux
from pathlib import Path
from uxarray.grid.coordinates import _populate_centroid_coord

current_path = Path(os.path.dirname(os.path.realpath(__file__)))

gridfile_CSne8 = current_path / "meshfiles" / "scrip" / "outCSne8" / "outCSne8.nc"


class TestCentroids(TestCase):

    def test_centroids_from_mean_verts(self):
        # Create a triangle
        test_triangle = np.array([(0, 0, 1), (0, 0, -1), (1, 0, 0)])

        # Calculate the expected centroid
        expected_centroid = np.mean(test_triangle, axis=0)

        # Open the dataset and find the centroids
        grid = ux.open_grid(test_triangle)
        _populate_centroid_coord(grid)

        # Test the values of the calculate centroids
        self.assertEqual(expected_centroid[0], grid.Mesh2_face_cart_x)
        self.assertEqual(expected_centroid[1], grid.Mesh2_face_cart_y)
        self.assertEqual(expected_centroid[2], grid.Mesh2_face_cart_z)

    def test_centroids_from_mean_verts_scrip(self):
        """Test computed centroid values compared to values from a SCRIP
        dataset."""

        uxgrid = ux.open_grid(gridfile_CSne8)

        expected_face_x = uxgrid.Mesh2_face_x.values
        expected_face_y = uxgrid.Mesh2_face_y.values

        _populate_centroid_coord(uxgrid, repopulate=True)

        computed_face_x = uxgrid.Mesh2_face_x.values
        computed_face_y = uxgrid.Mesh2_face_y.values

        pass

        nt.assert_array_almost_equal(expected_face_x, computed_face_x)
        nt.assert_array_almost_equal(expected_face_y, computed_face_y)
