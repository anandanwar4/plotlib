import numpy as np;
import data.visualisation.matrix.BasicMatrixUtil as BasicMatrixUtil;

class VectorTransform:

    basic_matrix_util = BasicMatrixUtil();

    def get_transformed_vector(self, vector: list, basis_matrix_from: np.ndarray, basis_matrix_to: np.ndarray) -> list:
        """Returns transformed vector with given to basis.

        Args:
            vector (sequence): vector to be transformed.
            basis_matrix_from (np.ndarray): matrix representing basis matrix of given vector.
            basis_matrix_to (np.ndarray): matrix representing destination basis matrix.

        Return:
            Transformed vector (sequence).
        """

        vector_in_normal_basis = np.multiply(basis_matrix_from, vector);
        vector_in_to_basis = np.multiply(
            self.basic_matrix_util.get_inverse_of_matrix(basis_matrix_to), vector_in_normal_basis);
        return vector_in_to_basis;

    def get_transformed_vector(self, vector: list, basis_matrix_from: np.ndarray) -> list:
        """Returns transformed vector to normal basis.

        Args:
            vector (sequence): vector to be transformed.
            basis_matrix_from (np.ndarray): matrix representing basis matrix of given vector.

        Return:
            Transformed vector (sequence).
        """

        return np.multiply(basis_matrix_from, vector);