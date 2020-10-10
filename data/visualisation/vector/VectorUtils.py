import math


class VectorUtils:
    def get_magnitude(self, vector: list) -> float:
        """Returns the magnitude of the vector.

        Args:
            vector (list): Vector for which magnitude has to be found.

        Return:
            Magnitude(float) of the vector.
        """

        sum_of_squares = 0;
        for ele in vector:
            sum_of_squares = sum_of_squares + (ele * ele);
        return math.sqrt(sum_of_squares);

    def get_unit_vector(self, vector: list) -> list:
        """Returns the unit vector of given vector.

        Args:
            vector (list): Vector for which unit vector has to be found.

        Return:
            Unit vector(list) of the given vector.
        """

        magnitude = self.get_magnitude(vector);
        unit_vector = [(ele / magnitude) for ele in vector];
        return unit_vector;

    def scalar_multiply(self, multiplier: float, vector: list) -> list:
        """Returns vector after scalar multiplication.

        Args:
            multiplier (float): Number by which vector has to be multiplied.
            vector (list): Vector for which multiplied vector has to be found.

        Return:
            Enhanced vector(list) after multiplication of scalar vector with the given vector.
        """

        enhanced_vector = [(multiplier * ele) for ele in vector];
        return enhanced_vector;

    def add_vectors(self, vector1: list, vector2: list) -> list:
        """Return an added vector.

        Args:
            vector1 (list): first vector.
            vector2 (list): second vector.

        Return:
            Added vector (list).
        """

        if (not len(vector1) == len(vector2)):
            raise IndexError("Vectors passed should be of the same size. "
                             "Length found: length of vector1 = " + len(vector1)
                             + "and length of vector2 = " + len(vector2));
        added_vector = [(vector1.__getitem__(index) + vector2.__getitem__(index)) for index in range(len(vector1))];
        return added_vector;

    def subtract_vectors(self, vector1: list, vector2: list) -> list:
        """Return the subtracted vector (vector1 - vector2).

        Args:
            vector1 (list): first vector.
            vector2 (list): second vector.

        Return:
            Subtracted vector (list).
        """

        if (not len(vector1) == len(vector2)):
            raise IndexError("Vectors passed should be of the same size. "
                             "Length found: length of vector1 = " + len(vector1)
                             + "and length of vector2 = " + len(vector2));
        subtracted_vector = [(vector1.__getitem__(index) - vector2.__getitem__(index)) for index in range(len(vector1))];
        return subtracted_vector;

    def dot_product(self, vector1: list, vector2: list) -> float:
        """Return the dot product of given vectors.

        Args:
            vector1 (list): first vector.
            vector2 (list): second vector.

        Return:
            Dot product(float) of vectors.
        """

        if (not len(vector1) == len(vector2)):
            raise IndexError("Vectors passed should be of the same size. "
                             "Length found: length of vector1 = " + len(vector1)
                             + "and length of vector2 = " + len(vector2));
        dot_product = 0;
        for index in range(len(vector1)):
            dot_product = dot_product + (vector1.__getitem__(index) * vector2.__getitem__(index));
        return dot_product;

    def get_projection(self, vector1: list, vector2: list) -> list:
        """Returns projection of vector1 on vector2

        Args:
            vector1 (list): first vector.
            vector2 (list): second vector.

        Return:
            Projection (list) of vector1 on vector2.
        """

        magnitude_vector1_squared = math.pow(self.get_magnitude(vector2), 2);
        magnitude_of_projection = self.dot_product(vector1, vector2) / magnitude_vector1_squared;
        projection = self.scalar_multiply(magnitude_of_projection, vector2);
        return projection;


def test_get_magnitude():
    vector_utils = VectorUtils();
    list = [3, 4];
    magnitude = vector_utils.get_magnitude(list);
    assert(magnitude == 5);

def test_get_unit_vector():
    vector_utils = VectorUtils();
    list = [3, 4];
    unit_vector = vector_utils.get_unit_vector(list);
    print(unit_vector);

def test_scalar_multiply():
    vector_utils = VectorUtils();
    list = [3, 4];
    enhanced_vector = vector_utils.scalar_multiply(2, list);
    assert(enhanced_vector.__getitem__(0) == 6);
    assert (enhanced_vector.__getitem__(1) == 8);

def test_add_vectors():
    vector_utils = VectorUtils();
    list1 = [3, 4];
    list2 = [4, 5];
    added_vector = vector_utils.add_vectors(list1, list2);
    assert(added_vector.__getitem__(0) == 7);
    assert (added_vector.__getitem__(1) == 9);

def test_subtract_vectors():
    vector_utils = VectorUtils();
    list1 = [3, 4];
    list2 = [4, 5];
    subtracted_vector = vector_utils.subtract_vectors(list1, list2);
    assert(subtracted_vector.__getitem__(0) == -1);
    assert (subtracted_vector.__getitem__(1) == -1);

def test_dot_product():
    vector_utils = VectorUtils();
    list1 = [3, 4];
    list2 = [4, 5];
    dot_prod = vector_utils.dot_product(list1, list2);
    assert(dot_prod == 32);

def test_get_projection():
    vector_utils = VectorUtils();
    list1 = [3, 4];
    list2 = [4, 5];
    projection_vector = vector_utils.get_projection(list1, list2);
    print(projection_vector);

test_get_magnitude();
test_get_unit_vector();
test_scalar_multiply();
test_add_vectors();
test_subtract_vectors();
test_dot_product();
test_get_projection();





