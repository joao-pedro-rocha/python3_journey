m = float(input('\nDigite uma distância em metros: '))
km = m / 10 / 10 / 10
hm = m / 10 / 10
dam = m / 10
dm = m * 10
cm = m * 10 * 10
mm = m * 10 * 10 * 10

print(' ')
print('{} M corresponde a: \n\n{:<8} Km. \n{:<8} Hm. \n{:<8} Dam. \n{:<8} Dm. \n{:<8} Cm. \n{:<8} Mm.'.format(m, km, hm, dam, dm, cm, mm))