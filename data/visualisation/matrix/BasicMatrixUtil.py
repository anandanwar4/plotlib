import numpy as np;

class BasicMatrixUtil:
    def get_combined_matrix_from_vectors(self, vector1, vector2, *args: list, rowwise = True) -> np.ndarray:
        """Combines given vectors into a matrix.

        User for combining multiple vectors into a single matrix. \
        By default the combination is row wise. Combination can be \
        specified to be column wise by specifying rowwise parameter as False.

        Args:
            vector1 (Sequence): First vector.\n
            vector2 (Sequence): Second vector.\n
            *args (Sequences): Additional vectors if needed.\n
            rowwise (bool): By default - True. Vectors will be combined row-wise \
            if set to true and column-wise otherwise.
        """

        list_of_vectors = list();
        list_of_vectors.append(vector1);
        list_of_vectors.append(vector2);
        for vector in args:
            list_of_vectors.append(vector);
        arr = np.array(list_of_vectors);
        if (not rowwise):
            return arr.T;
        return arr;


    def get_identity_matrix(self, rows: int, type: object) -> np.ndarray:
        """Returns Identity matrix.

        Used to get identity matrix of the specified dimensions(rows) \
        and the given type.

        Args:
            rows (int): Number of rows in matrix.\n
            type (object): Allowed values - int/float. The matrix \
            elements will be of the given type.
        """

        dType = np.float64;
        if (issubclass(type, int)):
            dType = np.int64;
        return np.identity(rows, dType);


    def get_determinant_of_matrix(self, array: np.ndarray) -> float:
        """Returns determinant of matrix.

        Args:
            array (np.ndarray): Matrix whose determinant has to be calculated.
        """

        return np.linalg.det(array);


    def get_inverse_of_matrix(self, array: np.ndarray) -> np.ndarray:
        """Return inverse of given array.

        Args:
            array (np.ndarray): Matrix whose inverse has to be calculated.
        """

        return np.linalg.pinv(array);


def test_get_combined_matrix_from_vectors_with_two_vectors():
    obj = BasicMatrixUtil();
    list1 = [1, 2, 3, 4];
    list2 = [2, 2, 3, 5];
    arr = obj.get_combined_matrix_from_vectors(list1, list2, rowwise=True);
    print(arr);

def test_get_identity_matrix():
    rows = 3;
    obj = BasicMatrixUtil();
    print(obj.get_identity_matrix(rows, int));
    print(obj.get_identity_matrix(rows, float));

def test_get_determinant_of_matrix():
    arr = np.array([(1., 2.), (2., 3.)]);
    obj = BasicMatrixUtil();
    print(obj.get_determinant_of_matrix(arr));

def test_get_inverse_of_matrix():
    arr = np.array([(1., 2.), (4., 3.)]);
    obj = BasicMatrixUtil();
    print(obj.get_inverse_of_matrix(arr));


test_get_combined_matrix_from_vectors_with_two_vectors();
test_get_identity_matrix();
test_get_determinant_of_matrix();
test_get_inverse_of_matrix();
