1. GPU was 11x faster than CPU
2. running it on colab
3. number of parameters = memory (bytes) / bytes per parameter

Free GPU Memory = 15 * 1024^3 ~ 15,024,586,752 bytes
Bytes per Parameter (FP16) = 2 bytes
(15,024,586,752 / 2) / 1,000,000,000 ≈ 7.51 Billion Parameters
