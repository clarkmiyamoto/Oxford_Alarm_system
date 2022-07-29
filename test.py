
from Oxford_Triton import Oxford_Triton

triton = Oxford_Triton(name='triton',
                file_path='/Users/clarkmiyamoto/Desktop/_code/LFL_Research/Oxford log/log 220526 172110.vcl',
                magnet=False)

print(triton.temperature_mixing_chamber())
