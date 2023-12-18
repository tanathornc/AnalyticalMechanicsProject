import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from tqdm import tqdm
from scipy.interpolate import griddata
from matplotlib import cm
import scipy.ndimage as ndimage

plt.rc('text', usetex=True)
fig = plt.figure()
ax = plt.axes(projection='3d')


def integrand(E,k,theta):
	return np.sqrt(2)/np.emath.sqrt(E+ k/2*np.sin(theta)**2 + np.cos(theta))


def T(E,k,lod=3000):
	theta = np.linspace(0, np.pi, lod)


	inte = np.trapz(integrand(E, k, theta), dx = np.pi/lod).real
	if inte == 0:
		#if the real part is zero, this means that the motion is not possible, take it to nan so we wont plot it.
		return np.nan
	return inte

def plot_withRange(E_min, E_max, k_min, k_max, lod = 100, sigma_denoise = 1.0, order_denoise = 0):
	E = np.linspace(E_min,E_max, lod)
	k = np.linspace(k_min,k_max ,lod)
	x, y = np.meshgrid(E,k)
	z = np.zeros((lod,lod))

	for i in tqdm(range(lod)):
		for j in range(lod):
			z[i,j]=  2*np.sqrt(2)*T(x[i,j], y[i,j])

	#add a Gaussian noise filter to smooth out.
	z = ndimage.gaussian_filter(z, sigma = sigma_denoise, order=order_denoise)

	ax = plt.axes(projection='3d')
	ax.set_xlabel(r'$\tilde{E}$', fontsize=13)
	ax.set_ylabel('$k$', fontsize=13)
	ax.set_zlabel('$T$', fontsize=13)

	ax.plot_surface(x ,y,z, rstride=1, cstride=1,
	                cmap='viridis', edgecolor='none',linewidth=0)

	ax.set_title('Oscilation Period');

	plt.show()
	return z





