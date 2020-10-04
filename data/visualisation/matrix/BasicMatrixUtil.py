import numpy as np;

class BasicMatrixUtil:
    def getCombinedMatrixFromVectors(self, vector1, vector2, *args: list, rowwise = True) -> np.ndarray:
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

        listOfVectors = list();
        listOfVectors.append(vector1);
        listOfVectors.append(vector2);
        for vector in args:
            listOfVectors.append(vector);
        arr = np.array(listOfVectors);
        if (not rowwise):
            return arr.T;
        return arr;


    def getIdentityMatrix(self, rows: int, type: object) -> np.ndarray:
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


    def getDeterminantOfMatrix(self, array: np.ndarray) -> float:
        """Returns determinant of matrix.

        Args:
            array (np.ndarray): Matrix whose determinant has to be calculated.
        """

        return np.linalg.det(array);


    def getInverseOfMatrix(self, array: np.ndarray) -> np.ndarray:
        """Return inverse of given array.

        Args:
            array (np.ndarray): Matrix whose inverse has to be calculated.
        """

        return np.linalg.pinv(array);


def testGetCombinedMatrixFromVectorsWithTwoVectors():
    obj = BasicMatrixUtil();
    list1 = [1, 2, 3, 4];
    list2 = [2, 2, 3, 5];
    arr = obj.getCombinedMatrixFromVectors(list1, list2, rowwise=True);
    print(arr);

def testGetIdentityMatrix():
    rows = 3;
    obj = BasicMatrixUtil();
    print(obj.getIdentityMatrix(rows, int));
    print(obj.getIdentityMatrix(rows, float));

def testGetDeterminantOfMatrix():
    arr = np.array([(1., 2.), (2., 3.)]);
    obj = BasicMatrixUtil();
    print(obj.getDeterminantOfMatrix(arr));

def testGetInverseOfMatrix():
    arr = np.array([(1., 2.), (4., 3.)]);
    obj = BasicMatrixUtil();
    print(obj.getInverseOfMatrix(arr));


testGetCombinedMatrixFromVectorsWithTwoVectors();
testGetIdentityMatrix();
testGetDeterminantOfMatrix();
testGetInverseOfMatrix();
