class DemoClass:
    def __init__(self, name):
        self.name = name

    # return and validate string (which is an HTTP header)
    def return_data(self) -> str:
        return f"{{name: {self.name}, data: hello}}"

    @staticmethod
    def vector_sum(a: tuple, b: tuple) -> tuple:
        """Compute sum of two Vector3 objects

        :param a: Vector3 object
        :type a: tuple
        :param b: Vector3 object
        :type b: tuple
        """
        return a[0] + b[0], a[1] + b[1], a[2] + b[2]

    @staticmethod
    def scale_vector(scale: int, vector: tuple) -> tuple:
        """Scale a Vector3 object

        :param scale: Scale factor
        :type scale: int
        :param vector: Vector3 object
        :type vector: tuple
        :return: Scaled Vector3 object
        :rtype: tuple
        """
        return scale * vector[0], scale * vector[1], scale * vector[2]

    @staticmethod
    def sum_and_callback(a: tuple, b: tuple, callback) -> None:
        """Compute sum of two Vector3 objects and pass to callback

        :param a: Vector3 object
        :type a: tuple
        :param b: Vector3 object
        :type b: tuple
        :param callback: Callback function
        :type callback: function
        """
        callback(DemoClass.vector_sum(a, b))
