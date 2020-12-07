main() {
  int val = 5;
  double value = 6;
  // if (val < 6) {
  //   throw Exception('Walao, can bigger or not');
  // }

  try {
    val *= 100;
  } on Exception catch (e) {
    print('Errorrrrrr');
  } finally {
    print('Walao eh World');
    print(val);
  }
}
