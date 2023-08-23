from demo import demo_class


def main() -> None:
    demo = demo_class.DemoClass('Demo')
    demo.return_data()
    print(demo.return_data())
    print(demo.vector_sum((1, 2, 3), (4, 5, 6)))
    print(demo.scale_vector(2, (1, 2, 3)))
    demo.sum_and_callback((1, 2, 3), (4, 5, 6), print)


if __name__ == '__main__':
    main()
